// Empty JS for your own code to be here

  
  // Call updateImage() when a change takes place to the DOM
  d3.selectAll("#btn").on("change", updateImage);
  
  // This function is called when a dropdown menu item is selected
  function updateImage() {
    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#btn");
    // Assign the value of the dropdown menu option to a variable
    var dataset = dropdownMenu.property("value");
    // if statements to determine image
    
  }
  
 
  