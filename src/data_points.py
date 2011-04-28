import package_data_point
import class_data_point
import method_data_point
import os

class DataPoints():

  # The metric groups used
  methodMetrics = ["MLOC", "NBD", "VG", "PAR"]
  classMetrics = ["NORM", "NOF", "NSC", "NOM", "DIT", "LCOM", "NSM", "SIX", "WMC", "NSF"]
  packageMetrics = ["NOC", "CA", "NOI", "RMI", "CE", "RMD", "RMA"]
  overallMetrics = ["NOP", "TLOC"]

  # Method Data: [name, MLOC, NBD, VG, PAR]
  methodData = []

  # Class Data: [name, NORM, NOF, NSC, NOM, DIT, LCOM, NSM, SIX, WMC, NSF]
  classData = []

  # Package Data: [name, NOC, CA, NOI, RMI, CE,  RMD, RMA]
  packageData = []

  def write_labels(self, lableFile, data):
    for dataPoint in data:
      lableFile.write(str(getattr(dataPoint,"name")) + '\n')

  def write_to_libsvm(self, dataFile, data, metrics):
    dataFile.write('#' + repr(metrics) + '\n')
    for dataPoint in data:
      fileCount = 1
      dataFile.write('-1')
      for i in range(len(metrics)):
        dataFile.write(' ' + str(fileCount) + ':' + str(getattr(dataPoint, metrics[i])))
        fileCount += 1
      dataFile.write('\n')

  def write_values(self, fileName, fileType):

    methodFile = open(fileName + '_method.' + fileType, 'w')
    classFile = open(fileName + '_class.' + fileType, 'w')
    packageFile = open(fileName + '_package.' + fileType, 'w')

    if fileType == "libsvm":
      self.write_to_libsvm(methodFile, self.methodData, self.methodMetrics)
      self.write_to_libsvm(classFile, self.classData, self.classMetrics)
      self.write_to_libsvm(packageFile, self.packageData, self.packageMetrics)
    elif fileType == "csv":
      self.write_to_libsvm(methodFile, self.methodData, self.methodMetrics)
      self.write_to_libsvm(classFile, self.classData, self.classMetrics)
      self.write_to_libsvm(packageFile, self.packageData, self.packageMetrics)
    else:
      raise Exception("ERROR UNKNOWN OUTPUT TYPE", userArgs.outputType)

    methodFile.close()
    classFile.close()
    packageFile.close()

    # Write out the labels (names) for the data
    methodLabelsFile = open(fileName + '_method_lables', 'w')
    classLabelsFile = open(fileName + '_class_lables', 'w')
    packageLabelsFile = open(fileName + '_package_lables', 'w')

    self.write_labels(methodLabelsFile, self.methodData)
    self.write_labels(classLabelsFile, self.classData)
    self.write_labels(packageLabelsFile, self.packageData)

  def write_to_csv(self, fileName):
    Exception("NOT YET IMPLEMENTED")

  def method_index(self, name):
    index = 0
    for dataPoint in self.methodData:
      if dataPoint.name == name:
        return index
      index += 1
    return -1

  def class_index(self, name):
    index = 0
    for dataPoint in self.classData:
      if dataPoint.name == name:
        return index
      index += 1
    return -1

  def package_index(self, name):
    index = 0
    for dataPoint in self.packageData:
      if dataPoint.name == name:
        return index
      index += 1
    return -1

  def add_method_data(self, metric, name, value):
    index = self.method_index(name)
    if index == -1:
      # Add new method to data set
      self.methodData.append(method_data_point.MethodDataPoint())
      self.methodData[index].name = name
      setattr(self.methodData[index], metric, value)
    else:
      # Add value to existing data set
      setattr(self.methodData[index], metric, value)

  def add_class_data(self, metric, name, value):
    index = self.class_index(name)
    if index == -1:
      # Add new class to data set
      self.classData.append(class_data_point.ClassDataPoint())
      self.classData[index].name = name
      setattr(self.classData[index], metric, value)
    else:
      # Add value to existing data set
      setattr(self.classData[index], metric, value)

  def add_package_data(self, metric, name, value):
    index = self.package_index(name)
    if index == -1:
      # Add new package to data set
      self.packageData.append(package_data_point.PackageDataPoint())
      self.packageData[index].name = name
      setattr(self.packageData[index], metric, value)
    else:
      # Add value to existing data set
      setattr(self.packageData[index], metric, value)
