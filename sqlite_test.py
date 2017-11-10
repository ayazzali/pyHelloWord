import sqlite3
import logging as log

log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=log.INFO)
# log.setLoggerClass("sqlite-test-log")

def CreateTable(conn):
    cursor=conn.cursor()
    res=cursor.execute("""Create table IF NOT EXISTS mytable
        (question text, answer text, date text)""" )
    log.info("table creted")
    log.info(res)

def InsertTrashData(conn):
    cursor=conn.cursor()
    cursor.execute("delete from mytable")
    cursor.execute("""Insert into mytable
    values('привет', 'Привет! спроси меня что нибудь, а я постараюсь тебе выдать полезную информацию по твоему вопросу', datetime('now'))""" )
    conn.commit()
    log.info("insert one is done")

    faq=[('кто я?', 'думаю ты студент', 'now')]
    cursor.executemany('INSERT INTO mytable values(?,?,datetime(?))',faq)
    conn.commit()
    log.info("insert many is done")

def Select(conn):
    cur = conn.cursor()
    log.info("select * from mytable:")
    cur.execute("select * from mytable")  
    log.info(cur.fetchall())

def UpdateNoCommit(conn):
    """не коммитим изменения - тоесть [грубо] после перезапуска порграммы всё останется как было"""
    c=conn.cursor()
    c.execute("""update mytable
    
    set date= datetime('now')
    where question ='привет' 
    """)
    log.info('update Done')




def __main__():
    conn = sqlite3.connect("dbname")
    # CreateTable(conn)
    # InsertTrashData(conn)
    Select(conn)
    UpdateNoCommit(conn)
    Select(conn)

log.info("__name__ is: "+__name__)
if __name__=="__main__":
    __main__()