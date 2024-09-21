import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from wordcloud import WordCloud
from io import BytesIO
import base64
import pandas as pd

def create_wordcloud(domains):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(domains))
    img = BytesIO()
    wordcloud.to_image().save(img, format='PNG')
    return base64.b64encode(img.getvalue()).decode()


def create_dashboard(results):
    app = dash.Dash(__name__)
    
    options = [{'label': k, 'value': k} for k in results.keys()] if results else []

    app.layout = html.Div([
        dcc.Dropdown(
            id='keyword-dropdown',
            options=options,
            value=options[0]['value'] if options else None
        ),
        dcc.Graph(id='bar-chart'),
        dcc.Graph(id='bubble-chart'),
        dcc.Graph(id='sunburst-chart'),
        html.Div(id='processing-time'),
        html.Div([
            html.H3('Word Cloud of Matched Domains'),
            html.Img(id='matched-wordcloud-img')
        ]),
        html.Div([
            html.H3('Word Cloud of Unmatched Domains'),
            html.Img(id='unmatched-wordcloud-img')
        ])
    ])

    @app.callback(
        Output('bar-chart', 'figure'),
        Output('bubble-chart', 'figure'),
        Output('sunburst-chart', 'figure'),
        Output('matched-wordcloud-img', 'src'),
        Output('unmatched-wordcloud-img', 'src'),
        Output('processing-time', 'children'),  # New output for processing time
        Input('keyword-dropdown', 'value')
    )
    def update_charts(selected_keyword):
        if selected_keyword and selected_keyword in results:
            keyword_results = results[selected_keyword]
            matched_domains = keyword_results['matched_domains']
            unmatched_domains = keyword_results['unmatched_domains']

            matched_counts = [len(matched_domains)]
            unmatched_counts = [len(unmatched_domains)]

            bar_fig = px.bar(x=[selected_keyword], y=[matched_counts, unmatched_counts], barmode='group', labels={'x': 'Keywords', 'y': 'Number of Domains'},
                            title='Matched and Unmatched Domains by Keyword')

            bubble_data = [
                {'keyword': selected_keyword, 'count': len(matched_domains), 'type': 'Matched'},
                {'keyword': selected_keyword, 'count': len(unmatched_domains), 'type': 'Unmatched'}
            ]
            bubble_fig = px.scatter(pd.DataFrame(bubble_data), x='keyword', y='count', size='count', color='type', title='Bubble Chart of Domains by Keyword')

            sunburst_data = [
                {'keyword': selected_keyword, 'domain': domain, 'type': 'Matched'} for domain in matched_domains
            ] + [
                {'keyword': selected_keyword, 'domain': domain, 'type': 'Unmatched'} for domain in unmatched_domains
            ]
            sunburst_fig = px.sunburst(pd.DataFrame(sunburst_data), path=['keyword', 'type', 'domain'], title='Domain Distribution by Keyword and Match Type')

            if matched_domains:
                matched_wordcloud_img = 'data:image/png;base64,' + create_wordcloud(matched_domains)
            else:
                matched_wordcloud_img = None
            
            if unmatched_domains:
                unmatched_wordcloud_img = 'data:image/png;base64,' + create_wordcloud(unmatched_domains)
            else:
                unmatched_wordcloud_img = None

            # Display processing time
            processing_time = f"Processing Time: {keyword_results['process_time']:.2f} seconds"

            return bar_fig, bubble_fig, sunburst_fig, matched_wordcloud_img, unmatched_wordcloud_img, processing_time
        else:
            return {}, {}, {}, None, None, None

    app.run_server(debug=False)
