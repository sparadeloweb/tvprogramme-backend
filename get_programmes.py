import xml.etree.ElementTree as ET

def parseXML (xmlfile):
    tree = ET.parse(xmlfile) # Parseo el XML con la herramienta importada

    root = tree.getroot() # Obtengo la raiz el arbol

    channels = [] # Array a llenar

    # Obtengo todos los canales

    for channel in root.findall('channel'):

        channelToAdd = {}

        channelToAdd['name'] = channel.find('display-name').text # Obtengo nombre del canal

        icon = channel.find('icon')

        if(icon != None): # Si tiene icono obtengo su URL
            channelToAdd['logo_src'] = channel.find('icon').attrib['src']

        channelToAdd['id'] = channel.attrib['id'] # Obtengo el ID del programa
        
        channels.append(channelToAdd)

    programmes = [] # Array a llenar

    # Obtengo todos los programas

    for programme in root.findall('programme'):

        programmeToAdd = {}

        programmeToAdd['channel_id'] = programme.attrib['channel'] # Obtengo el ID del canal para asociar

        programmeToAdd['start_time'] = programme.attrib['start'] # Obtengo el tiempo de inicio formateado

        programmeToAdd['finish_time'] = programme.attrib['stop'] # Obtengo el tiempo de finalizacion formateado

        titles = programme.findall('title')

        programmeToAdd['main_title'] = titles[0].text # Obtengo titulo del programa

        if(len(titles) > 1): # Si tiene un titulo en ingles / idioma original se lo agrega
            programmeToAdd['original_title'] = titles[1].text

        subtitle = programme.find('sub-title') # Busco los subtitulos del programa

        if(subtitle != None): # Si tiene subtitulo lo agrego
            programmeToAdd['subtitle'] = subtitle.text


        desc = programme.find('desc') # Obtengo la descripcion

        if(desc != None): # Si tiene descripcion, lo agrego
            programmeToAdd['description'] = desc.text 

        image = programme.find('icon') # Busco la imagen

        if(image != None): # Si tiene imagen, la agrego
            programmeToAdd['image'] = image.attrib['src']

        frenchCategories = programme.findall("category[@lang='fr']") # Busco las categorias en frances

        programmeToAdd['category'] = frenchCategories[0].text # Agrego la categoria principal
        
        if(len(frenchCategories) > 1): # Si tiene mas de una categoria
            programmeToAdd['sub_category'] = frenchCategories[1].text # Agrego la subcategoria

        englishCategory = programme.find("category[@lang='en']") # Busco las categorias en ingles

        if(englishCategory != None): # Si tiene una categoria en ingles, se la agrego
            programmeToAdd['original_category'] = englishCategory.text

        date = programme.find('date') # Busco la fecha

        if(date != None): # Si tiene fecha lo agrego
            programmeToAdd['year_date'] = date.text

        country = programme.findall('country')

        if(len(country)):
            programmeToAdd['country'] = country[0].text
        
        programmes.append(programmeToAdd)

    # Una vez termino de ejecutar unifico todo
    for channel in channels:

        channel['programmes'] = []

        for programme in programmes:

            if(programme['channel_id'] == channel['id']):
                
                channel['programmes'].append(programme)

    return channels