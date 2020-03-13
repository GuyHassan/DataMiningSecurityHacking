import eel
import json
from createUrlPage import createUrlPage

url_temporary = "https://www.a1securitycameras.com/technical-support/default-username-passwords-ip-addresses-for-surveillance-cameras/"

eel.init('webFolder')

@eel.expose  # Expose this function to Javascript
def getLinkFromSite(urlAddress):
    # create a class that include all the backend in the code
    sites = createUrlPage()
    # get the data from the site
    DataFromSites = sites.GoDeep(str(urlAddress), 1)
    print(DataFromSites)
    # export the data to the file data.json
    with open('webFolder\data.json', 'w') as outfile:
        json.dump(DataFromSites, outfile)
    return None


eel.start('FinalProject.html', size=(1300, 700), mode='chrome-app', port=9090,
          cmdline_args=['--start-fullscreen', '--browser-startup-dialog']).Default: []
