{% extends 'base.html' %} {% block content %}
<br>
<br>
<div class="container">
    
    <div class="row col s6">
        <h1>Add Recipe</h1>
    </div>
    
</div>

<div class="container">
    <br>
        <div class="row">
            
            <div class="container">
            <div class="form-group">
                <form action="{{ url_for('insert_record') }}" id="form1" method="POST" class="col s12" enctype="multipart/form-data">
                    
                    <div class="row m12">
                        
                        <div class="col s6"> 
                            <h3>Upload an image for your recipe:</h3>
                            <input id="file" name="file" type="file" >
                        </div>
                    </div>
                    
                    <br>
                    <br>

                    <div class="row col s6" label for="icon_prefix">
                        <div class="input-field col s6">
                            <strong> User Name (Full) </strong> 
                                <input id="user_name" name="user_name" type="text">
                        </div>
                    </div>
                    
                            
                    <div class="row col s6" label for="icon_prefix">
                        <div class="input-field col s6">
                            <strong> Recipe Name </strong> 
                                <input id="recipe_name" name="recipe_name" type="text">
                        </div>
                    </div>
                     
                    
                    <div class="row col s6" label for="icon_prefix">
                        <div class="input-field col s6">
                            <strong> Preparation Time </strong>
                                <input id="prep_time" name="prep_time" type="text">
                        </div>
                    </div>
                   
        
                    <div class="row col s6" label for="icon_prefix">
                        <div class="input-field col s6">
                             <strong> Portion Sizes </strong>
                                 <input id="portion_size" name="portion_size" type="text">
                        </div>
                    </div>
                    
                    
                    <div class="row col s12" label for="icon_prefix">
                        <div class="col s6">
                            <strong> Food Type </strong>
                                    <select id="food_category" name="food_category" class="icons">
                                        <option value="Meat" data-icon="https://s3-us-west-2.amazonaws.com/data-centic-development-storage/category_images/meat_eaters.jpg">Meat</option>
                                        <option value="Vegetarian" data-icon="https://s3-us-west-2.amazonaws.com/data-centic-development-storage/category_images/vegetarian.jpg">Vegetarian</option>
                                        <option value="Keto" data-icon="https://s3-us-west-2.amazonaws.com/data-centic-development-storage/category_images/keto.jpg">Keto</option>
                                        <option value="Paleo" data-icon="https://s3-us-west-2.amazonaws.com/data-centic-development-storage/category_images/paleo.jpg">Paleo</option>
                                        <option value="Asian Fusion" data-icon="https://s3-us-west-2.amazonaws.com/data-centic-development-storage/category_images/asian_fusion.jpg">Asian Fusion</option>
                                        <option value="Middle Eastern" data-icon="https://s3-us-west-2.amazonaws.com/data-centic-development-storage/category_images/middle_eastern.jpg">Middle Eastern</option>
                                        <option value="European" data-icon="https://s3-us-west-2.amazonaws.com/data-centic-development-storage/category_images/european.jpg">European</option>
                                        <option value="Desert" data-icon="https://s3-us-west-2.amazonaws.com/data-centic-development-storage/category_images/desert.jpg">Desert</option>
                                    </select>
                        </div>
                    </div>
                        

                    <div class="row col s12" label for="icon_prefix">
                        <br>
                            <div class="input-field col s6">
                                <strong> Recipe Description </strong>
                                    <textarea name="recipe_description" input id="recipe_description" class="materialize-textarea"></textarea>
                            </div>
                    </div>
                        
                            
                    <div class="row col s12" label for="icon_prefix">
                        <br>
                            <div class="input-field col s6">
                                <strong> Ingredients (Put each ingredient on a new line) </strong>
                                    <textarea name="recipe_ingredients" input id="recipe_ingredients" class="materialize-textarea"></textarea>
                            </div>
                    </div>
                    
                    
                    <div class="row col s12" label for="icon_prefix">
                        <br>
                            <div class="input-field col s6">
                                <strong> Utensils (Place each item on a new line) </strong>
                                    <textarea name="utensils" input id="utensils" class="materialize-textarea"></textarea>
                            </div>
                    </div>
                    
                    
                    <div class="row col s12" label for="icon_prefix">
                        <br>
                            <div class="input-field col s6">
                                <strong> Allergins (Place each item on a new line) </strong>
                                    <textarea name="allergins" input id="allergins" class="materialize-textarea"></textarea>
                            </div>
                    </div>
                    
                    
                    <div class="row col s12" label for="icon_prefix">
                        <br>
                            <div class="input-field col s6">
                                <strong> Nutrition Per Serving (Place each item on a new line) </strong>
                                    <textarea name="nutrition" input id="nutrition" class="materialize-textarea"></textarea>
                            </div>
                    </div>
                                
                            
                    <div class="row col s12" label for="icon_prefix">
                        <br>
                            <div class="input-field col s6">
                                <strong> Directions (Put each direction on a new line) </strong>
                                    <textarea name="recipe_directions" input id="recipe_directions" class="materialize-textarea"></textarea>
                            </div>
                    </div>
                    
                    <br>
                    
                    <div class="row col s12">
                        <button class="btn waves-effect waves-light" type="submit"> 
                            <input id="submit" type="submit" value="Submit">
                        </button>
                    </div>
                    

                </form>
                    
            </div>
            
            
            </div>
</div>