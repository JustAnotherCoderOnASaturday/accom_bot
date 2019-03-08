from Pages import accom_pages


def pageOrder():
    ''' Put the Page order in here'''
    pass


if __name__ == '__main__':
    getUrl = input("Copy/Paste URL: ")
    now = accom_pages(getUrl)
    now.getSite()

