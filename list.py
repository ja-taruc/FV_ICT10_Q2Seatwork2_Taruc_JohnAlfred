from pyscript import window, display

def general_weighted_average(event=None):
    doc = window.document

    # Student info
    fname = doc.getElementById("fname").value
    lname = doc.getElementById("lname").value
    glevel = doc.getElementById("glevel").value

    # Grades
    science = float(doc.getElementById("sci").value)
    english = float(doc.getElementById("eng").value)
    ict = float(doc.getElementById("ict").value)
    math = float(doc.getElementById("math").value)
    filipino = float(doc.getElementById("filo").value)
    pe = float(doc.getElementById("pe").value)

    # Weighted computation
    weighted_sum = (
        science * 5 +
        math * 5 +
        english * 5 +
        filipino * 3 +
        ict * 2 +
        pe * 1
    )

    total_units = 5 + 5 + 5 + 3 + 2 + 1
    gwa = weighted_sum / total_units

    # Summary
    summary = f"""
Science : {science}
Math    : {math}
English : {english}
Filipino: {filipino}
ICT     : {ict}
PE      : {pe}
"""

    # Display output
    display(
        f"<b>Name:</b> {fname} {lname}<br><b>Grade Level:</b> {glevel}",
        target="result"
    )

    display(
        f"<pre>{summary}</pre><h3>GWA: {gwa:.2f}</h3>",
        target="status"
    )
