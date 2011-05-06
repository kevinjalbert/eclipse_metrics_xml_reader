from lxml import etree
import data_points
import argparse
import os

# Holds user arguments
userArgs = None

# Make data point object
dataPoints = data_points.DataPoints()

def handleMethod(metricGroup):

  # Acquire list of the overall value of a metric group
  for overallValue in metricGroup:

    # Acquire list of individual values
    for value in overallValue:

      # Acquire absolute name
      name = value.get("package") + "." + value.get("source").replace(".java", "") + "." + value.get("name")
      dataPoints.add_method_data(metricGroup.get("id"), name, value.get("value"))

def handleClass(metricGroup):

  # Acquire list of the overall value of a metric group
  for overallValue in metricGroup:

    # Acquire list of individual values
    for value in overallValue:

      # Acquire absolute name
      name = value.get("package") + "." + value.get("name")
      dataPoints.add_class_data(metricGroup.get("id"), name, value.get("value"))

def handlePackage(metricGroup):

  # Acquire list of the overall value of a metric group
  for overallValue in metricGroup:

    # Acquire list of individual values
    for value in overallValue:
      dataPoints.add_package_data(metricGroup.get("id"), value.get("name"), value.get("value"))

def handleOverall(metricGroup):

  # Acquire the overall values of this metric group
  for overallValue in metricGroup:

    pass #print metricGroup.get("id"), overallValue.get("value")
    # TODO Add values to data points in a category with the overall values

def main():

  # Read in the XML file
  tree = etree.parse(userArgs.inputFile)
  root = tree.getroot()

  # Acquire the project's name and the namespace
  projectName = root.get("scope")
  namespace = "{http://metrics.sourceforge.net/2003/Metrics-First-Flat}"

  # Acquire list of metric groups
  for metricGroup in root:

    # Filter out the cycle element as it just contains the packages
    if metricGroup.tag == namespace + "Cycle":
      continue

  # Call the appropriate handle function for this metric group
    if metricGroup.get("id") in dataPoints.methodMetrics:
      handleMethod(metricGroup)
    elif metricGroup.get("id") in dataPoints.classMetrics:
      handleClass(metricGroup)
    elif metricGroup.get("id") in dataPoints.packageMetrics:
      handlePackage(metricGroup)
    elif metricGroup.get("id") in dataPoints.overallMetrics:
      handleOverall(metricGroup)
    else:
      raise Exception("ERROR UNKNOWN METRIC", metricGroup.get("id"))

    print "[LOG] : Finished Reading " + metricGroup.get("id") + " Metrics"

  # Write file
  dataPoints.write_values(os.path.splitext(userArgs.inputFile)[0], userArgs.outputType)
  print "[LOG] : Finished Converting XML to " + userArgs.outputType

# If this module is ran as main
if __name__ == '__main__':

  # Define the argument options to be parsed
  parser = argparse.ArgumentParser(
      description = 'eclipse_metrics_xml_reader <https://github.com/kevinjalbert/eclipse_metrics_xml_reader>',
      version = 'eclipse_metrics_xml_reader 0.2.0')
  parser.add_argument(
      '-i',
      action='store',
      default=None,
      dest='inputFile',
      help='Input XML file to be read (product of Eclipse Metrics Plugin)')
  parser.add_argument(
      '-t',
      action='store',
      default='libsvm',
      dest='outputType',
      help='Output file type (Options: libsvm) [Default=libsvm]')

 # Parse the arguments passed from the shell
  userArgs = parser.parse_args()

  if userArgs.inputFile == None:
    raise Exception("ERROR NO INPUT FILE SPECIFIED")

  main()
