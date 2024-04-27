"""Pension simulator to guess how long until retirement."""
PENSION_AGE=65
print("Välkomna till denna pensionssimulator")
name = input("Vad heter du i förnamn?\n")
arg1 = input("Hur gammal är du?\n")
age = int(arg1)
your_pension = str(PENSION_AGE - age) # pylint: disable=invalid-name
print("Hej " + name + ". Du går i pension om " + your_pension + " år.")
