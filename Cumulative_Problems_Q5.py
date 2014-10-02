def date_converter(language, date):
    datelist = date.split("/")
    return str(datelist[1]) + " " + str(language[int(datelist[0])]) + " " + str(datelist[2])