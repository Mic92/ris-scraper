# encoding: utf-8

RS = "059110000000" #Bochum

# Stadtname für Logfile
CITY = 'bochum'

# Currently, only "mongodb" is supported
DB_TYPE = 'mongodb'

# Name of the MongoDB database
DB_NAME = 'ris'

# Use "localhost" if MongoDB is running on the same machine
DB_HOST = 'localhost'

# MongoDB default port is 27017
DB_PORT = 27017

# SessionNet base url, should include trailing slash
BASE_URL = 'https://session.bochum.de/bi/'

# Name to identify your crawler to the server
USER_AGENT_NAME = 'scrape-a-ris/0.1'

# Number of seconds to wait between requests. Increase this
# if the systems behaves unstable (seconds)
WAIT_TIME = 0.2

# Log level (DEBUG, INFO, WARNING, ERROR or CRITICAL)
LOG_LEVEL = 'INFO'

# File to log to
LOG_BASE_DIR = '/var/log/ris-scraper/'

#Scraper Type
SCRAPER_TYPE = 'SESSIONNET'



PARTY_ALIAS = {
  'GRU': u'Bündnis 90 / Die Grünen',
  u'Grüne': u'Bündnis 90 / Die Grünen',
  'DIE LINKE.': 'DIE LINKE',
  "\"Zuhause in Bochum\"": 'Zuhause in Bochum' 
}

###### Result normalization mapping

RESULT_STRINGS = {
  'Die Anfrage wird schriftlich beantwortet.': 'ANFAGE_ANTWORT_SCHRIFTLICH',
  'Die Anfrage ist schriftlich beantwortet worden.': 'ANFRAGE_BEANTWORTET_SCHRIFTLICH',
  u'Die Anfrage ist m\xfcndlich beantwortet worden.': 'ANFAGE_BEANTWORTET_MUENDLICH',
  u'Die Anfrage ist zur\xfcckgezogen worden.': 'ANFRAGE_RUECKZUG',
  
  'Die Mitteilung wird zur Kenntnis genommen.': 'MITTEILUNG_KENNTNIS',
  
  'Die Vorlage wird ohne Votum weitergeleitet.': 'VORLAGE_WEITERLEITUNG',
  u'Die Entscheidung \xfcber die Vorlage wird zur\xfcckgestellt.': 'VORLAGE_ZUERUECKGESTELLT',
  u'Die Verwaltung zieht die Vorlage zur\xfcck.': 'VORLAGE_RUECKZUG_VERWALTUNG',
  u'Die Vorlage wird zur\xfcck \xfcberwiesen.': 'VORLAGE_UEBERWEISUNG_ZURUECK',
  u'Die Vorlage wird an x \xfcberwiesen.': 'VORLAGE_UEBERWEISUNG',
  'Die Vorlage wird von der Tagesordnung abgesetzt.': 'VORLAGE_ABGESETZT',
  
  u'Der Antrag wird zur\xfcckgezogen.': 'ANTRAG_RUECKZUG',
  'Der Antrag ist gegenstandslos, daher keine Abstimmung.': 'ANTRAG_GEGENSTANSLOS',
  

  'kein Beratungsergebnis': 'BERATUNG_ERGEBNISLOS',
  u'Die Beratung der Vorlage wird zur\xfcckgestellt.': 'BERATUNG_ZUERUCKGESTELLT',
  
  u'Die Beschlussfassung wird teilweise zur\xfcckgestellt.': 'BESCHLUSS_ZURUECKGESTELLT_TEILWEISE',
  'Die Abstimmung erfolgte getrennt nach Unterpunkten.': 'ABSTIMMUNG_UNTERPUNKTE',
  
  'Abstimmungsergebnis: Einstimmig nach Beschlussvorschlag': 'BESCHLOSSEN_EINSTIMMIG',
  u'Abstimmungsergebnis: Einstimmig nach Erg\xe4nzung des Beschlussvorschlages':'BESCHLOSSEN_EINSTIMMIG_ERGAENZUNG',
  u'Abstimmungsergebnis: Einstimmig nach \xc4nderung des Beschlussvorschlages': 'BESCHLOSSEN_EINSTIMMIG_AENDERUNG',

  'Abstimmungsergebnis: Mehrheitlich nach Beschlussvorschlag': 'BESCHLOSSEN_MEHRHEIT',
  u'Abstimmungsergebnis: Mehrheitlich nach Erg\xe4nzung des Beschlussvorschlages':'BESCHLOSSEN_MEHRHEIT_ERGAENZUNG',
  u'Abstimmungsergebnis: Mehrheitlich nach \xc4nderung des Beschlussvorschlages': 'BESCHLOSSEN_MEHRHEIT_AENDERUNG',

  'Abstimmungsergebnis: Einstimmig gegen Beschlussvorschlag': 'ABGELEHNT_EINSTIMMIG',

  'Abstimmungsergebnis: Mehrheitlich gegen Beschlussvorschlag': 'ABGELEHNT_MEHRHEIT',
  
  'erledigt': 'ERLEDIGT'
}

##### Page URL masks

URLS = {
  'ASP': {
    # Month calender page
    'CALENDAR_MONTH_PARSE_PATTERN': 'si0040.asp?__cjahr={year:d}&__cmonat={month:d}',
    'CALENDAR_MONTH_PRINT_PATTERN': BASE_URL + 'si0040.asp?__cjahr=%d&__cmonat=%d',

    # Meeting detail page
    'SESSION_DETAIL_PARSE_PATTERN': 'to0040.asp?__ksinr={meeting_id:d}',
    'SESSION_DETAIL_PRINT_PATTERN': BASE_URL + 'to0040.asp?__ksinr=%d',

    # Committee detail page
    'COMMITTEE_DETAIL_PARSE_PATTERN': 'kp0040.asp?__kgrnr={committee_id:d}',
    'COMMITTEE_DETAIL_PRINT_PATTERN': BASE_URL + 'kp0040.asp?__kgrnr=%d',

    # Paper detail page
    'SUBMISSION_DETAIL_PARSE_PATTERN': 'vo0050.asp?__kvonr={paper_id:d}',
    'SUBMISSION_DETAIL_PRINT_PATTERN': BASE_URL + 'vo0050.asp?__kvonr=%d',
    
    # Attachment file download target file name(s)
    'ATTACHMENT_DOWNLOAD_TARGET': ['getfile.asp']
  },
  'PHP': {
    # Month calender page
    'CALENDAR_MONTH_PARSE_PATTERN': 'si0040.php?__cjahr={year:d}&__cmonat={month:d}',
    'CALENDAR_MONTH_PRINT_PATTERN': BASE_URL + 'si0040.php?__cjahr=%d&__cmonat=%d',

    # Meeting detail page
    'SESSION_DETAIL_PARSE_PATTERN': 'to0040.php?__ksinr={meeting_id:d}',
    'SESSION_DETAIL_PRINT_PATTERN': BASE_URL + 'to0040.php?__ksinr=%d',

    # Committee detail page
    'COMMITTEE_DETAIL_PARSE_PATTERN': 'kp0040.php?__kgrnr={committee_id:d}',
    'COMMITTEE_DETAIL_PARSE_PATTERN_FULL': 'kp0040.php?__cwp=1&__kgrnr={committee_id:d}',
    'COMMITTEE_DETAIL_PRINT_PATTERN': BASE_URL + 'kp0040.php?__kgrnr=%d',
    'COMMITTEE_DETAIL_PRINT_PATTERN_FULL': BASE_URL + 'kp0040.php?__cwpall=1&__kgrnr=%d',
    
    # Person overview page
    'PERSON_OVERVIEW_PARSE_PATTERN': 'kp0041.php?__cwpall=1',
    'PERSON_OVERVIEW_PRINT_PATTERN': BASE_URL + 'kp0041.php?__cwpall=1',

    # Person detail page
    'PERSON_DETAIL_PARSE_PATTERN': 'kp0051.php?__kpenr={person_id:d}',
    'PERSON_DETAIL_PRINT_PATTERN': BASE_URL + 'kp0051.php?__kpenr=%d',
    
    # Person committee page kp0050.php?__cwpall=1&__kpenr=1524
    'PERSON_COMMITTEE_PARSE_PATTERN': 'kp0050.php?__cwpall=1&__kpenr={person_id:d}',
    'PERSON_COMMITTEE_PRINT_PATTERN': BASE_URL + 'kp0050.php?__cwpall=1&__kpenr=%d',
    'PERSON_DETAIL_PARSE_PATTERN_ALT': 'kp0050.php?__kpenr={person_id:d}&grnr=0',
    'PERSON_DETAIL_PRINT_PATTERN_ALT': BASE_URL + 'kp0050.php?__kpenr=%d&grnr=0',

    # Paper detail page
    'SUBMISSION_DETAIL_PARSE_PATTERN': 'vo0050.php?__kvonr={paper_id:d}',
    'SUBMISSION_DETAIL_PRINT_PATTERN': BASE_URL + 'vo0050.php?__kvonr=%d',

    # Attachment file download target file name
    'ATTACHMENT_DOWNLOAD_TARGET': ['ydocstart.php', 'getfile.php']
  }
}


##### XPATH strings to find elements within pages

XPATH = {
  'ASP': {
    # session title within the session details page
    'SESSION_DETAIL_TITLE': '//h1',

    # table fields with session identifier, comittee name and more details
    'SESSION_DETAIL_IDENTIFIER_TD': '//*[@id="smctablevorgang"]/tbody//td',

    # link to committe within the session details page
    'SESSION_DETAIL_COMMITTEE_LINK': '//li[@class="smcmenucontext_fct_gremium"]/a',

    # table rows containing agendaitems on session detail page
    'SESSION_DETAIL_AGENDA_ROWS': '//*[@id="smc_page_to0040_contenttable1"]/tbody/tr',

    # link to submission in agenda item row on session detail page
    'SESSION_DETAIL_AGENDA_ROWS_SUBMISSION_LINK': 'td/a',

    # table with session-related attachment downloads on session detail page
    'SESSION_DETAIL_ATTACHMENTS': '//*[@id="smccontent"]/table',

    # distinct class of the box/table containing session-related attachment downloads
    'SESSION_DETAIL_ATTACHMENTS_CONTAINER_CLASSNAME': 'smcdocboxright',

    # Same as above, for the submission detail page (Vorlagen-Detailseite)
    'SUBMISSION_DETAIL_TITLE': '//h1',

    'SUBMISSION_DETAIL_IDENTIFIER_TD': '//*[@id="smctablevorgang"]/tbody//td',

    # "Beratungsfolge" table rows
    'SUBMISSION_DETAIL_AGENDA_ROWS': '//*[@id="smc_page_vo0050_contenttable1"]/tbody/tr',

    'SUBMISSION_DETAIL_ATTACHMENTS': '//*[@id="smccontent"]/table',

    'SUBMISSION_DETAIL_ATTACHMENTS_CONTAINER_CLASSNAME': 'smcdocboxright',
  },
  'PHP': {
    # session title within the session details page
    'SESSION_DETAIL_TITLE': '//h1',

    # table fields with session identifier, comittee name and more details
    'SESSION_DETAIL_IDENTIFIER_TD': '//*[@id="smctablevorgang"]/tbody//td',

    # link to committe within the session details page
    'SESSION_DETAIL_COMMITTEE_LINK': '//li[@class="smcmenucontext_fct_gremium"]/a',

    # table rows containing agendaitems on session detail page
    'SESSION_DETAIL_AGENDA_ROWS': '//*[@class="smccontenttable smc_page_to0040_contenttable"]/tbody/tr',

    # link to submission in agenda item row on session detail page
    'SESSION_DETAIL_AGENDA_ROWS_SUBMISSION_LINK': './/a',

    # table with session-related attachment downloads on session detail page
    'SESSION_DETAIL_ATTACHMENTS': '//*[@id="smccontent"]//table',

    # distinct class of the box/table containing session-related attachment downloads
    'SESSION_DETAIL_ATTACHMENTS_CONTAINER_CLASSNAME': 'smcdocbox',

    # Same as above, for the submission detail page (Vorlagen-Detailseite)
    'SUBMISSION_DETAIL_TITLE': '//h1',
    'SUBMISSION_DETAIL_IDENTIFIER_TD': '//*[@id="smctablevorgang"]/tbody//td',

    'PERSONLIST_LINES': '//table[@id="smc_page_kp0041_contenttable1"]//tr',
    
    'PERSON_COMMITTEE_LINES': '//table[@id="smc_page_kp0050_contenttable1"]//tr',

    # "Beratungsfolge" table rows
    'SUBMISSION_DETAIL_AGENDA_ROWS': '//*[@class="smccontenttable smc_page_vo0050_contenttable"]/tbody/tr',

    'SUBMISSION_DETAIL_ATTACHMENTS': '//*[@id="smccontent"]//table',

    'SUBMISSION_DETAIL_ATTACHMENTS_CONTAINER_CLASSNAME': 'smcdocbox'
  }
}

FILE_EXTENSIONS = {
  'application/pdf': 'pdf',
  'image/tiff': 'tif',
  'image/jpeg': 'jpg',
  'application/vnd.ms-powerpoint': 'pptx',
  'application/msword': 'doc',
  'application/zip': 'zip'
}
