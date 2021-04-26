import sqlite3

con = sqlite3.connect(input())
cur = con.cursor()
temp, rash = int(input()), int(input())
result = list(cur.execute('''SELECT temp,
                     rash, place_id FROM malaclaws WHERE temp >= ? AND rash <= ?''',
                          (temp, rash,)).fetchall())
for i in range(len(result)):
    place = cur.execute('''SELECT name FROM places WHERE id = ?''',
                        (result[i][2],)).fetchone()
    result[i] = [place[0], str(result[i][0]), str(result[i][1])]
result.sort(key=lambda x: (float(x[1]), x[0]), reverse=True)
for i in result:
    print(' '.join(i))
