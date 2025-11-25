from pyscript import document, display

def general_weighted_average(event=None):
    # Get student info
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value
    glevel = document.getElementById("glevel").value

    # Get grades
    science = float(document.getElementById("sci").value)
    english = float(document.getElementById("eng").value)
    ict = float(document.getElementById("ict").value)
    math = float(document.getElementById("math").value)
    filipino = float(document.getElementById("filo").value)
    pe = float(document.getElementById("pe").value)

    # Subject list (for summary)
    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]

    # Calculate weighted sum
    weighted_sum = (science * 5 +
                    math * 5 +
                    english * 5 +
                    filipino * 3 +
                    ict * 2 +
                    pe * 1)

    # Total weight/units
    total_units = (5 + 5 + 5 + 3 + 2 + 1)

    # GWA computation
    gwa = weighted_sum / total_units

    # Grade summary
    summary = f"""
Science : {science:.0f}
Math    : {math:.0f}
English : {english:.0f}
Filipino: {filipino:.0f}
ICT     : {ict:.0f}
PE      : {pe:.0f}
"""

    # Output results to HTML
    display(f"<b>Name:</b> {fname} {lname}<br><b>Grade:</b> {glevel}", target="result")
    display(f"<pre>{summary}</pre>", target="status")
    display(f"<h3>Your General Weighted Average is <b>{gwa:.2f}</b></h3>", target="status")
