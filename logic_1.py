# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True
def cigar_party(cigars, is_weekend):
    return ((not is_weekend and cigars >= 40 and cigars <= 60) or (is_weekend and cigars >= 40))
# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1
# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True
def squirrel_play(temp, is_summer):
  i = 0
  if is_summer: i = 10
  return(temp >= 60 and temp <= (90 + i))


# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21
def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <= 19:
    return 20
  return sum

# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'
def alarm_clock(day, vacation):
  if day in range(1,6):
    if vacation == False:
      return "7:00"
    elif vacation == True:
      return "10:00"
  else:
    if vacation == False:
      return "10:00"
    else:
      return "off"

# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True
def love6(a, b):
  for each in {a, b, a+b, a-b, b-a}:
    if each == 6: return True
  return False

# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True
def near_ten(num):
  return(num % 10 <= 2 or num % 10 >=8)






