from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from tensorflow import keras
#from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH ='birdsclassi.h5'

# Load your trained model
model = load_model(MODEL_PATH)


name_list = os.listdir(path='birddataset/Training/')
name_list = sorted(name_list)
#print(name_list)
ordinalname = {i:k for i,k in enumerate(name_list,0)}

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/birdgallery')
def birdgallery():
    return render_template('birdgallery.html')

@app.route('/exotic')
def exotic():
    return render_template('exotic.html')




def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    if preds[0][0] == 1:
        preds = 'AFRICAN FIREFINCH'
    elif preds[0][1] == 1:
        preds =  'ALBATROSS'
    elif preds[0][2] == 1:
        preds = 'ALEXANDRINE PARAKEET'
    elif preds[0][3] == 1:
        preds = 'AMERICAN AVOCET'
    elif preds[0][4] == 1:
        preds = 'AMERICAN BITTERN'
    elif preds[0][5] == 1:
        preds = 'AMERICAN COOT'
    elif preds[0][6] == 1:
        preds = 'AMERICAN GOLDFINCH'
    elif preds[0][7] == 1:
        preds = 'AMERICAN KESTREL'
    elif preds[0][8] == 1:
        preds = 'AMERICAN PIPIT'
    elif preds[0][9] == 1:
        preds = 'AMERICAN REDSTART'
    elif preds[0][10] == 1:
        preds = 'ANHINGA'
    elif preds[0][11] == 1:
        preds = 'ANNAS HUMMINGBIRD'
    elif preds[0][12] == 1:
        preds = 'ANTBIRD'
    elif preds[0][13] == 1:
        preds = 'ARARIPE MANAKIN'
    elif preds[0][14] == 1:
        preds = 'ASIAN CRESTED IBIS'
    elif preds[0][15] == 1:
        preds = 'BALD EAGLE'
    elif preds[0][16] == 1:
        preds = 'BALI STARLING'
    elif preds[0][17] == 1:
        preds = 'BALTIMORE ORIOLE'
    elif preds[0][18] == 1:
        preds = 'BANANAQUIT'
    elif preds[0][19] == 1:
        preds = 'BAR-TAILED GODWIT'
    elif preds[0][20] == 1:
        preds = 'BARN OWL'
    elif preds[0][21] == 1:
        preds = 'BARN SWALLOW'
    elif preds[0][22] == 1:
        preds = 'BAY-BREASTED WARBLER'
    elif preds[0][23] == 1:
        preds = 'BEARDED BARBET'
    elif preds[0][24] == 1:
        preds = 'BELTED KINGFISHER'
    elif preds[0][25] == 1:
        preds = 'BIRD OF PARADISE'
    elif preds[0][26] == 1:
        preds =  'BLACK FRANCOLIN'
    elif preds[0][27] == 1:
        preds = 'BLACK SKIMMER'
    elif preds[0][28] == 1:
        preds = 'BLACK SWAN'
    elif preds[0][29] == 1:
        preds = 'BLACK THROATED WARBLER'
    elif preds[0][30] == 1:
        preds = 'BLACK VULTURE'
    elif preds[0][31] == 1:
        preds =  'BLACK-CAPPED CHICKADEE'
    elif preds[0][32] == 1:
        preds = 'BLACK-NECKED GREBE'
    elif preds[0][33] == 1:
        preds = 'BLACK-THROATED SPARROW'
    elif preds[0][34] == 1:
        preds = 'BLACKBURNIAM WARBLER'
    elif preds[0][35] == 1:
        preds = 'BLUE GROUSE'
    elif preds[0][36] == 1:
        preds = 'BLUE HERON'
    elif preds[0][37] == 1:
        preds = 'BOBOLINK'
    elif preds[0][38] == 1:
        preds = 'BROWN NOODY'
    elif preds[0][39] == 1:
        preds = 'BROWN THRASHER'
    elif preds[0][40] == 1:
        preds = 'CACTUS WREN'
    elif preds[0][41] == 1:
        preds = 'CALIFORNIA CONDOR'
    elif preds[0][42] == 1:
        preds = 'CALIFORNIA GULL'
    elif preds[0][43] == 1:
        preds = 'CALIFORNIA QUAIL'
    elif preds[0][44] == 1:
        preds = 'CANARY'
    elif preds[0][45] == 1:
        preds = 'CAPE MAY WARBLER'
    elif preds[0][46] == 1:
        preds = 'CAPUCHINBIRD'
    elif preds[0][47] == 1:
        preds = 'CARMINE BEE-EATER'
    elif preds[0][48] == 1:
        preds = 'CASPIAN TERN'
    elif preds[0][49] == 1:
        preds = 'CASSOWARY'
    elif preds[0][50] == 1:
        preds =  'CHARA DE COLLAR'
    elif preds[0][51] == 1:
        preds = 'CHIPPING SPARROW'
    elif preds[0][52] == 1:
        preds = 'CINNAMON TEAL'
    elif preds[0][53] == 1:
        preds = 'COCK OF THE  ROCK'
    elif preds[0][54] == 1:
        preds =  'COCKATOO'
    elif preds[0][55] == 1:
        preds = 'COMMON GRACKLE'
    elif preds[0][56] == 1:
        preds = 'COMMON HOUSE MARTIN'
    elif preds[0][57] == 1:
        preds = 'COMMON LOON'
    elif preds[0][58] == 1:
        preds = 'COMMON POORWILL'
    elif preds[0][59] == 1:
        preds = 'COMMON STARLING'
    elif preds[0][60] == 1:
        preds = 'COUCHS KINGBIRD'
    elif preds[0][61] == 1:
        preds = 'CRESTED AUKLET'
    elif preds[0][62] == 1:
        preds = 'CRESTED CARACARA'
    elif preds[0][63] == 1:
        preds = 'CROW'
    elif preds[0][64] == 1:
        preds = 'CROWNED PIGEON'
    elif preds[0][65] == 1:
        preds = 'CUBAN TODY'
    elif preds[0][66] == 1:
        preds = 'CURL CRESTED ARACURI'
    elif preds[0][67] == 1:
        preds = 'D-ARNAUDS BARBET'
    elif preds[0][68] == 1:
        preds = 'DARK EYED JUNCO'
    elif preds[0][69] == 1:
        preds = 'DOWNY WOODPECKER'
    elif preds[0][70] == 1:
        preds = 'EASTERN BLUEBIRD'
    elif preds[0][71] == 1:
        preds = 'EASTERN MEADOWLARK'
    elif preds[0][72] == 1:
        preds = 'EASTERN ROSELLA'
    elif preds[0][73] == 1:
        preds = 'EASTERN TOWEE' 
    elif preds[0][74] == 1:
        preds = 'ELEGANT TROGON'
    elif preds[0][75] == 1:
        preds =  'ELLIOTS  PHEASANT'
    elif preds[0][76] == 1:
        preds = 'EMPEROR PENGUIN'
    elif preds[0][77] == 1:
        preds = 'EMU'
    elif preds[0][78] == 1:
        preds = 'EURASIAN MAGPIE'
    elif preds[0][79] == 1:
        preds =  'EVENING GROSBEAK'
    elif preds[0][80] == 1:
        preds = 'FLAME TANAGER'
    elif preds[0][81] == 1:
        preds = 'FLAMINGO'
    elif preds[0][82] == 1:
        preds = 'FRIGATE'
    elif preds[0][83] == 1:
        preds = 'GILA WOODPECKER'
    elif preds[0][84] == 1:
        preds = 'GILDED FLICKER'
    elif preds[0][85] == 1:
        preds = 'GLOSSY IBIS'
    elif preds[0][86] == 1:
        preds = 'GOLD WING WARBLER'
    elif preds[0][87] == 1:
        preds = 'GOLDEN CHEEKED WARBLER'
    elif preds[0][88] == 1:
        preds = 'GOLDEN CHLOROPHONIA'
    elif preds[0][89] == 1:
        preds = 'GOLDEN EAGLE'
    elif preds[0][90] == 1:
        preds = 'GOLDEN PHEASANT'
    elif preds[0][91] == 1:
        preds = 'GOULDIAN FINCH'
    elif preds[0][92] == 1:
        preds = 'GRAY CATBIRD'
    elif preds[0][93] == 1:
        preds = 'GRAY PARTRIDGE'
    elif preds[0][94] == 1:
        preds = 'GREEN JAY'
    elif preds[0][95] == 1:
        preds = 'GREY PLOVER'
    elif preds[0][96] == 1:
        preds = 'GUINEAFOWL'
    elif preds[0][97] == 1:
        preds = 'HARPY EAGLE'
    elif preds[0][98] == 1:
        preds = 'HAWAIIAN GOOSE'
    elif preds[0][99] == 1:
        preds = 'HOODED MERGANSER'
    elif preds[0][100] == 1:
        preds = 'HOOPOES'
    elif preds[0][101] == 1:
        preds = 'HORNBILL'
    elif preds[0][102] == 1:
        preds = 'HORNED GUAN'
    elif preds[0][103] == 1:
        preds = 'HOUSE FINCH'
    elif preds[0][104] == 1:
        preds = 'HOUSE SPARROW'
    elif preds[0][105] == 1:
        preds = 'HYACINTH MACAW'
    elif preds[0][106] == 1:
        preds = 'IMPERIAL SHAQ'
    elif preds[0][107] == 1:
        preds = 'INCA TERN'
    elif preds[0][108] == 1:
        preds = 'INDIAN BUSTARD'
    elif preds[0][109] == 1:
        preds = 'INDIGO BUNTING'
    elif preds[0][110] == 1:
        preds = 'JABIRU'
    elif preds[0][111] == 1:
        preds = 'JAVAN MAGPIE'
    elif preds[0][112] == 1:
        preds = 'KAKAPO'
    elif preds[0][113] == 1:
        preds = 'KILLDEAR'
    elif preds[0][114] == 1:
        preds = 'KING VULTURE'
    elif preds[0][115] == 1:
        preds = 'KIWI'
    elif preds[0][116] == 1:
        preds = 'LARK BUNTING'
    elif preds[0][117] == 1:
        preds = 'LEARS MACAW'
    elif preds[0][118] == 1:
        preds = 'LILAC ROLLER'
    elif preds[0][119] == 1:
        preds = 'LONG-EARED OWL'
    elif preds[0][120] == 1:
        preds ='MALACHITE KINGFISHER'
    elif preds[0][121] == 1:
        preds = 'MALEO'
    elif preds[0][122] == 1:
        preds = 'MALLARD DUCK'
    elif preds[0][123] == 1:
        preds =  'MANDRIN DUCK'
    elif preds[0][124] == 1:
        preds = 'MARABOU STORK'
    elif preds[0][125] == 1:
        preds = 'MASKED BOOBY'
    elif preds[0][126] == 1:
        preds = 'MIKADO  PHEASANT'
    elif preds[0][127] == 1:
        preds = 'MOURNING DOVE'
    elif preds[0][128] == 1:
        preds =  'MYNA'
    elif preds[0][129] == 1:
        preds = 'NICOBAR PIGEON'
    elif preds[0][130] == 1:
        preds ='NORTHERN CARDINAL'
    elif preds[0][131] == 1:
        preds = 'NORTHERN FLICKER'
    elif preds[0][132] == 1:
        preds = 'NORTHERN GANNET'
    elif preds[0][133] == 1:
        preds = 'NORTHERN GOSHAWK'
    elif preds[0][134] == 1:
        preds = 'NORTHERN JACANA'
    elif preds[0][135] == 1:
        preds = 'NORTHERN MOCKINGBIRD'
    elif preds[0][136] == 1:
        preds =  'NORTHERN PARULA'
    elif preds[0][137] == 1:
        preds = 'NORTHERN RED BISHOP'
    elif preds[0][138] == 1:
        preds ='OCELLATED TURKEY'
    elif preds[0][139] == 1:
        preds =  'OSPREY'
    elif preds[0][140] == 1:
        preds = 'OSTRICH'
    elif preds[0][141] == 1:
        preds = 'PAINTED BUNTIG'
    elif preds[0][142] == 1:
        preds =  'PALILA'
    elif preds[0][143] == 1:
        preds = 'PARADISE TANAGER'
    elif preds[0][144] == 1:
        preds = 'PARUS MAJOR'
    elif preds[0][145] == 1:
        preds = 'PEACOCK'
    elif preds[0][146] == 1:
        preds = 'PELICAN'
    elif preds[0][147] == 1:
        preds = 'PEREGRINE FALCON'
    elif preds[0][148] == 1:
        preds = 'PHILIPPINE EAGLE'
    elif preds[0][149] == 1:
        preds = 'PINK ROBIN'
    return preds
    

@app.route('/index', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)