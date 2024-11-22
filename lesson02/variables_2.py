                                # Memory
x = 1          # x [ ]------------>[ 1 ]

x = 3.14       # x [ ]             [ 1 ]   <-- no longer referenced
               #    |------------->[3.14]


print(x)      # x [ ]             -----   <-- garbage collected
               #    |------------->[3.14]

del(x)        # ----             -----   <-- garbage collected
               #    |------------->----  <--- all garbage collected

# print(x)      # NameError, x is no longer defined