class PackageDataPoint(object):
  name = None
  NOC = 0
  CA = 0
  NOI = 0
  RMI = 0
  CE = 0
  RMD = 0
  RMA = 0

  def to_string(self):
    return self.name, self.NOC, self.CA, self.NOI, self.RMI, self.CE, self.RMD, self.RMA
