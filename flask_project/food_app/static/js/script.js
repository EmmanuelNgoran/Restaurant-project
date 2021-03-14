// Developed at agap2
// Based on:
// http://www.codeply.com/go/s3I9ivCBYH/multi-carousel-single-slide-bootstrap-4

$('.multi-item-carousel').on('slide.bs.carousel', function (e) {
  let $e = $(e.relatedTarget),
      itemsPerSlide = 3,
      totalItems = $('.carousel-item', this).length,
      $itemsContainer = $('.carousel-inner', this),
      it = itemsPerSlide - (totalItems - $e.index());
  if (it > 0) {
    for (var i = 0; i < it; i++) {
      $('.carousel-item', this).eq(e.direction == "left" ? i : 0).
        // append slides to the end/beginning
        appendTo($itemsContainer);
    }
  }
});

/* Responsive mobile navbar */

const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener('click', () => {
  navbarLinks.classList.toggle('active')
})

/*AJAX request on a server end point */
const search_btn= $("#md_btn_submit");
const search_text_input = document.querySelector(".search_restaurant_input");
const search_city_input = $(".search_city_input");
const content_option = document.querySelector("#result_opt");

function search_match(){

  if(search_text_input.value.length > 0)
  {

    $.ajax({
      type: 'GET',
      url: '/api/search',
      data: {
        content:  search_text_input.value,
        city: search_city_input.val()
      },
      contentType: "application/json",
      dataType: 'json',
    
      success: function(data)
      {
          content_option.innerHTML=outputHtml(data);
      },
      error: function()
      {
          alert('Error');
      },
      complete: function()
      {
          //alert('Complete')
      }
    });
  }

  else{
    content_option.innerHTML="";
  }
  
}
function outputHtml(contents){
  let html="";
  if(contents.length)
  {
     html = contents.map(ele=>`<a  href='/resto/update/${ele['id']}'>
     <div class='card card-body mb-2'>
                  <h4>${ele['name']}</h4>
                  </div>
     </a>`).join('');
    return html;
        
  }
  else{
    html=`<div class='card card-body mb-2'>
    <h4>Nothing found</h4>
    </div>`;
  }
  return html
}
search_text_input.addEventListener('input',search_match);


