class MethodDataPoint(object):
  name = None
  MLOC = 0
  NBD = 0
  VG = 0
  PAR = 0

  def to_string(self):
    return self.name, self.MLOC, self.NBD, self.VG, self.PAR
