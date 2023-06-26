$(document).ready(function() {
    $('#rating-form').on('submit', function(e) {
      e.preventDefault(); // Prevent the form from submitting normally
  
      var stars = $('#stars-input').val();
  
      $.ajax({
        type: 'POST',
        url: '{% url "rate_product" %}',
        data: {
          stars: stars,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
          // Handle the success response here
          console.log('Rating submitted successfully');
        },
        error: function(xhr, status, error) {
          // Handle any error that occurs during the AJAX request
          console.error(error);
        }
      });
    });
  });