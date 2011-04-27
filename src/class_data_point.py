class ClassDataPoint(object):
  name = None
  NORM = 0
  NOF = 0
  NSC = 0
  NOM = 0
  DIT = 0
  LCOM = 0
  NSM = 0
  SIX = 0
  WMC = 0
  NSF = 0

  def to_string(self):
    return self.name, self.NORM, self.NOF, self.NSC, self.NOM, self.DIT, self.LCOM, self.NSM, self.SIX, self.WMC, self.NSF
