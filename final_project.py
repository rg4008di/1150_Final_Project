"""Random Taco Recipe Book Final Project Sunny Reum. I will be creating a program that will randomly generate taco recipes
 and a picture of a taco."""

# bring in the things
import requests
import docx

url = 'https://taco-1150.herokuapp.com/random/?full_taco=true' # Here i am setting the api in a variable.
foo = ['First', 'Second', 'Third']
document = docx.Document()  # create a new blank document

document.add_paragraph('Random Taco Cookbook', 'Title')
document.add_picture('tacos_resize.jpg', width=docx.shared.Inches(6), height=docx.shared.Inches(6))



document.add_paragraph('Code by: Sunny Reum', 'List Bullet')
document.add_paragraph('Image by: TJ Dragotta on Unsplash', 'List Bullet')
document.add_paragraph('Recipes from: https://taco-1150.herokuapp.com/random/?full_taco=true', 'List Bullet')
document.add_page_break()


for i in range(3):
    taco_recipe = requests.get(url).json()  # Then creating a variable to request the taco recipe.
    seasoning_name = taco_recipe['seasoning']['name']
    seasoning = taco_recipe['seasoning']['recipe']
    condiment_name = taco_recipe['condiment']['name']
    condiment = taco_recipe['condiment']['recipe']
    mixin_name = taco_recipe['mixin']['name']
    mixin = taco_recipe['mixin']['recipe']
    base_layer_name = taco_recipe['base_layer']['name']
    base_layer = taco_recipe['base_layer']['recipe']
    shell_name = taco_recipe['shell']['name']
    shell = taco_recipe['shell']['recipe']
    document.add_paragraph(f'{foo[i]} Taco Recipe', 'Title')
    document.add_paragraph(seasoning_name, 'Heading 1')
    document.add_paragraph(seasoning)
    document.add_paragraph(condiment_name, 'Heading 1')
    document.add_paragraph(condiment)
    document.add_paragraph(mixin_name, 'Heading 1')
    document.add_paragraph(mixin)
    document.add_paragraph(base_layer_name, 'Heading 1')
    document.add_paragraph(base_layer)
    document.add_paragraph(shell_name, 'Heading 1')
    document.add_paragraph(shell)
    document.add_page_break()

document.save('recipe.docx')




