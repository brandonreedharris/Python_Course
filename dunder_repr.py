class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self): #formatted string
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self): # raw data
    return f"Invoice({self.client}, {self.total})"


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))