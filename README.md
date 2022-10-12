# echo-label

Web app for labelling of echocardiography video clips (A4C).

## How to use

Run the app by running:

`python app.py`

Use the selection buttons to grade the clip according to the various criteria (see [Focused Critical Care Echocardiography: Development and Evaluation of an Image Acquisition Assessment Tool](https://pubmed.ncbi.nlm.nih.gov/26825858/))

Select the LV wall segments that are well defined (by clicking relevant sections on the image).

Press the `Segments done` button and press the `Submit` button. The selection will be recorded in a csv file in the `results` folder and a new image will be loaded.
### See examples

Good and bad examples for each criteria can be seen by pressing `Show me some examples`.


