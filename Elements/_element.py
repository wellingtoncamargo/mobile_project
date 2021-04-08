from selenium.webdriver.common.by import By

# Primeira tela
addPlanta = (By.ID, 'com.google.samples.apps.sunflower:id/add_plant')
toolBar = (By.ID, 'com.google.samples.apps.sunflower:id/toolbar')
plantList = (By.XPATH, '//android.widget.LinearLayout[@content-desc="Plant list"]')
myGarden = (By.XPATH, '//android.widget.LinearLayout[@content-desc="My garden"]')
emptyGarden = (By.ID, 'com.google.samples.apps.sunflower:id/empty_garden')

# Segunda tela

listaPlantas = (By.ID, 'com.google.samples.apps.sunflower:id/plant_item_title')
filterZone = (By.ID, 'com.google.samples.apps.sunflower:id/filter_zone')
