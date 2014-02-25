from datetime import date 


def is_valid_date(datestring):
    chunks = datestring.split('/')
    if len(chunks) != 3:
        return False
    if len(chunks[1]) > 2:
        return False
    return True

def is_lefty(datestring):
    chunks = datestring.split('/')
    if len(chunks[0]) > 2:
        return True
    if len(chunks[2]) > 2:
        return False
    else:
        return None

def rotate(chunks, dryrun=False):
    if dryrun:
        return chunks
    else:
        return tuple(reversed(chunks))

def earlier_date(d1, d2):
    if d1 <= d2:
        return d1
    else:
        return d2

def as_safest_date(datestring):
    chunks = map(int, datestring.split('/'))
    if is_lefty(datestring) is None:
        d1 = date(*chunks).replace(year=chunks[0]+2000) # we assume its 2082 if given 82
        d2 = date(*rotate(chunks)).replace(year=chunks[2]+2000)
        return earlier_date(d1, d2)
    if is_lefty(datestring):
        return date(*chunks)
    if not is_lefty(datestring):
        return date(*rotate(chunks))
    
if __name__ == '__main__':
   import sys
   for line in sys.stdin:
	try:
            print as_safest_date(line)
        except:
            print line.strip() + ' is illegal'
