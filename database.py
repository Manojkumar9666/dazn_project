import sqlite3


# Function to create a table
def create_table():
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        
        cur.execute('''
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Function to insert data into the links table
def insert_data(domains):
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        
        for domain in domains:
            cur.execute('INSERT INTO links (domain) VALUES (?)', (domain,))
        
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Domain data to insert
domain_data = [
    'visionsport.xyz',
    'livesoccer.pk',
    'sslivetv.com',
    'cric2watch.com',
    'watch.crichd.run',
    'latestupdatespk.com',
    'nowsportv.com',
    'stream2watch.pk',
    'mycricket.pk',
    'paktech2.com',
    'b.freestreams-live.my',
    'rojadirectatvonline.com',
    'freeshot.live',
    'dihd.so',
    'crichdlivecricket.com',
    'cricfoot2.com',
    'ronaldo7.me',
    'idn.gdplayertv.to',
    'crichd.info',
    'buffstreams.is',
    'footybite.tv',
    'nowmetv.com',
    'tvhd.tutvlive.info',
    'us.messitv.net',
    'sportskeeda.vip',
    'dihd.life',
    'vercanalestvgratis.com',
    'tutiehd4.com',
    'telerium.biz',
    'lacasadeltikitaka.net',
    'nowsports.me',
    '24freetv.com',
    '35tudeportetvhd.com',
    'rojadirectaenvivo.mx',
    'rojadirectaenvivo.la',
    'rojadirectaenvivo.cc',
    'c.freestreams-live.my',
    'sporttuna.online',
    'rojadirecta.at',
    'nowsports.co.in',
    'antennasports.ru',
    'telerium.de',
    'livetv.quest',
    'centralareana.live',
    'antenatv.store',
    'antenasport.shop',
    'rusticotv.xyz',
    'volkalive.ru',
    'daddy stream vuz',
    'rojadirectalive.tv',
    'ww1.tarjetarojatvonline.sx',
    'pirlotv.at',
    'hoca4u.xyz',
    'torkudomlu.foroactivo.com',
    'jepsikuydo3.foroactivo.com',
    'euro2024direct.ru',
    'rippleamu4.shop',
    'one-stream.shop',
    '61vipstreamer.shop',
    'buddycenters.shop',
    'rainostream4u.shop',
    'soccerstreams2.click',
    'hesgoaltv.org',
    'btvsports.lol',
    'freestreams-live1.im',
    '68donelfantastic.github.io',
    'mega-deportes.net',
    'nebunexa.com',
    'portalbarranca.com',
    'televisioncaleta.com',
    'verfutboltv.net',
    'todopelotatv.net',
    'freestreams-live.ga',
    'rodrixtv.info',
    'pirlotv.re',
    'wixstream.com',
    '123iptv.tv',
    'xhzb.tw',
    'dlhd.online',
    'zonadeportiva.xyz',
    '1.deporte libre.org',
    'tvspacehd.com',
    'fullchannels.online',
    'dihd.sx',
    'tv3.duktek.online',
    'football-germany.duktek.online',
    'plagiarismchecker.pk',
    'nowsportv.nl',
    'television libre.online',
    '1.sporthd.me',
    'promoshn.com',
    'bigsport.xyz',
    'newsw.site',
    'johnystream.live',
    'apkship.xyz',
    '1ststream.live',
    'pandasteams.live',
    'rojadirectatv.la',
    'rojadirecta.nl',
    'tarjetarojatvenvivo.pl',
    'rojadirectatv.sbs',
    'rojadirectatvonline.de',
    'tvfutbol.info',
    'rojadirectatvonline.club',
    'mundialqatar2022.tv',
    'pirlotv.uno',
    'danix1610.com',
    'rojadirectatvonline.pl',
    'rusosport.com',
    'jepsikuydo4.foroactivo.com',
    'poscitechs.shop',
    'love2live.wideiptv.top',
    '115ddy1.onlinehdhls.ru',
    'fakestream.co.in',
    '117ddh2.onlinehdhis.ru',
    'v2.sportsonline.si',
    'webhdrunns.onlinehdhis',
    '4kwebplay.xyz',
    'ddh1.mizhls.ru',
    'ddh2.mizhis.ru',
    'ddy1.mizhls.ru',
    'ddy3.mizhis.ru',
    'webhdrunns.mizhls.ru',
    'mhdsports.nl',
    '1qwebplay.xyz',
    'lewblivehdplay.ru',
    'otjb0606.xyz',
    'nlv.visualtv.eu',
    'mo3ad.xyz',
    'vipegor.top',
    'pltvsu.info',
    'newlife3.wanicelife.com',
    'rv.therevenge.co',
    'goldiptvofficiel.tv',
    'td3wb1bchdvsahp.ngolp',
    'dkyoctjcddxshli469r.org',
    'qmaalhy7acgxwhm.ngolp',
    'dkyoctjcddxhli469r.org',
    'zeusplay.life',
    'fullassia.com',
    'topembed.pw',
    'soccer100.shop',
    'worldsports4u.shop',
    'feedzstream.com',
    'reditsports.com',
    's1.sportea.link'
]

# Create the table
#create_table()

# Insert the domain data
#insert_data(domain_data)


# Function to fetch and display data from the links table
def fetch_data():
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM links')
        rows = cur.fetchall()
        print(rows)
        
        
        domains = [row[1] for row in rows]  # Extract domains from fetched rows
        return domains
            
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def table():
# Connect to your database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Query to get the list of tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all results
    tables = cursor.fetchall()
    print(tables)

    # Print the list of tables
    for table in tables:
     print(table[0])

    # Close the connection
    conn.close()

import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matched_domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS unmatched_domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
import sqlite3
import logging

# Function to insert a matched domain
def insert_matched_domain(domain):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO matched_domains (domain)
            VALUES (?)
        ''', (domain,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        logging.error(f"SQLite error: {e}")
    finally:
        conn.close()

# Function to insert an unmatched domain
def insert_unmatched_domain(domain):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO unmatched_domains (domain)
            VALUES (?)
        ''', (domain,))
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"SQLite error: {e}")
    finally:
        conn.close()

create_table()

#insert_data(domain_data)  first run manually[uncommet it] i am pusshing the data into links db table to validate the extract data 

# Call the setup function to create tables


# Fetch and display the data




