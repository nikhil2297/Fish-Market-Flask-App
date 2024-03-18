$(document).ready(function() {
    $("#prediction-form").submit(function(event) {
      event.preventDefault(); // Prevent default form submission
  
      const length1 = $("#length").val();
      const length2 = $("#length").val();
      const length3 = $("#length").val();
      const height = $("#height").val();
      const width = $("#width").val();
      const weight = $("#weight").val();
  
      const data = {
        weight,
        length1,
        length2,
        length3,
        height,
        width
      };
  
      $.ajax({
        url: "/predict",  type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function(response) {
          $("#prediction-result").text(`Predicted Species: ${response.predicted_species}`);
        },
        error: function(error) {
          console.error(error);
          $("#prediction-result").text("Prediction failed. Please try again.");
        }
      });
    });
  });