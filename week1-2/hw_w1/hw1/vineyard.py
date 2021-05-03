print("Enter the following quantities in feet.")
long = float(input("  How long is this row? "))
wide = float(input("  How wide is the end-post assembly? "))
space = float(input("  How much space should be between the vines? "))
V = int((long-2*wide)/space);
print("")
print("This row has enough space for",V,"vine(s).")
