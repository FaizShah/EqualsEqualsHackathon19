def foodScan(url):
    """Detects web annotations given an image, using the geotag metadata
        in the image to detect web entities."""
    import io
    from google.cloud.vision import types
    from google.cloud import vision
        
    client = vision.ImageAnnotatorClient()
    path = 'apple1.jpg'
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    
    web_detection_params = vision.types.WebDetectionParams(
        include_geo_results=True)
    image_context = vision.types.ImageContext(
        web_detection_params=web_detection_params)

    response = client.web_detection(image=image, image_context=image_context)

#    _score = format(response.web_detection.web_entities[0].score)
    _description = format(response.web_detection.web_entities[0].description)
    print(_description)

    return _description





