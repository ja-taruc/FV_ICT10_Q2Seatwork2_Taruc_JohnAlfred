from pyscript import document, display

def general_weighted_average(e):
   fname = document.getElementById('fname').value
   lname = document.getElementById('lname').value
   science = float(document.getElementById('science').value)
   english = float(document.getElementById('english').value)
   ict = float(document.getElementById('ict').value)
    math = float(document.getElementById('math').value)
   filipino = float(document.getElementById('filipino').value)
   pe = float(document.getElementById('pe').value)
   # these were recommeded by co pilot

weighted_sum = (science * 5 + math * 5 + english * 5 + filipino * 3 + ict * 2 + pe * 1)
total_units = (5 * 3) + 3 + 2 + 1
gwa = weighted_sum / total_units

display(f'Name: {first_name} {last_name}', target="student_info")
display(summary, target='summary')
display(f'Your general weighted average is {gwa:.2f}', target='output')

summary = f"""{subjects[0]}: {science:.0f}
{subjects[1]}: {math:.0f}
{subjects[2]}: {english:.0f}
{subjects[3]}: {filipino:.0f}
{subjects[4]}: {ict:.0f}
{subjects[5]}: {pe:.0f}
    """
display(fullname: {first_name} {last_name}', target="student_info")
display(summary, target='summary')
display(f'Your general weighted average is {gwa:.2f}', target='output')
