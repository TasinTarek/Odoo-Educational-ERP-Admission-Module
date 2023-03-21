// Next
function nextSection() {
          var currentSection = document.querySelector('section[style*="display: block"]');
          
          if(currentSection.getAttribute('id') === "section1") {
            // document.getElementById('section2').scrollIntoView({behavior: 'smooth'});
            document.getElementById("section2").style.display = "block";
            
            document.querySelector('.color2').style.backgroundColor = 'lightblue';
          } else if (currentSection.getAttribute('id') === "section2") {
            document.getElementById("section3").style.display = "block";
            document.querySelector('.color3').style.backgroundColor = 'lightblue';
          } else if (currentSection.getAttribute('id') === "section3") {
            document.getElementById("section4").style.display = "block";
            document.querySelector('button:last-child').style.display = "none";
            document.querySelector('.color4').style.backgroundColor = 'lightblue'; // hide "next" button on last section
          }
          
          currentSection.style.display = "none";
          document.querySelector('button:first-child').style.display = "block"; // show "previous" button when moving forward
         
        }
// Previous
function prevSection() {
            var currentSection = document.querySelector('section[style*="display: block"]');
            console.log(currentSection);
            if(currentSection.getAttribute('id') === "section2") {
                document.getElementById("section1").style.display = "block";
                document.querySelector('button:first-child').style.display = "none"; // hide "previous" button on first section
                
            } else if (currentSection.getAttribute('id') === "section3") {
              document.getElementById("section2").style.display = "block";
              
            } else if (currentSection.getAttribute('id') === "section4") {
                document.getElementById("section3").style.display = "block";
                
                document.querySelector('button:last-child').style.display = "block"; // show "next" button when moving back from last section
            }

            currentSection.style.display = "none"
            document.querySelector('button:last-child').style.display = "block"; // show "next" button when moving backward
            window.history.scrollRestoration = 'manual';
}
    // var bachelorOption = document.getElementById("bachelorOption");
    // var bachelorForm = document.getElementById("bachelorForm");

    // bachelorOption.addEventListener("click", function() {
    //     bachelorForm.style.display = "block";
    // });
// To Show The Selected Field
// function showSelectedValue(selectTag, targetId) {
//   var selectedOption = selectTag.options[selectTag.selectedIndex].text;
//   var targetElement = document.getElementById(targetId);
//   targetElement.innerHTML = selectedOption;

// }

// Addresses


// const checkbox = document.querySelector('#permanent-checkbox');
// const presentAddress = document.querySelector('#present-address');
// const presentZip = document.querySelector('#present-zip');
// const presentDistrict = document.querySelector('#present-district');
// const presentCountry = document.querySelector('#present-country');
// const permanentAddress = document.querySelector('#permanent-address');
// const permanentZip = document.querySelector('#permanent-zip');
// const permanentDistrict = document.querySelector('#permanent-district');
// const permanentCountry = document.querySelector('#permanent-country');

// checkbox.addEventListener('click', () => {
//   if (checkbox.checked) {
//     permanentAddress.value = presentAddress.value;
//     permanentZip.value = presentZip.value;
//     permanentDistrict.value = presentDistrict.value;
//     permanentCountry.value = presentCountry.value;
//     permanentAddress.disabled = true;
//     permanentZip.disabled = true;
//     permanentDistrict.disabled = true;
//     permanentCountry.disabled = true;
//   } else {
//     permanentAddress.value = '';
//     permanentZip.value = '';
//     permanentDistrict.value = '';
//     permanentCountry.value = '';
//     permanentAddress.disabled = false;
//     permanentZip.disabled = false;
//     permanentDistrict.disabled = false;
//     permanentCountry.disabled = false;
//   }
// });

// const checkbox = document.querySelector('#permanent-checkbox');
// const presentAddress = document.querySelector('#present-address');
// const permanentAddress = document.querySelector('#permanent-address');

// checkbox.addEventListener('click', () => {
//   if (checkbox.checked) {
//     permanentAddress.value = presentAddress.value;
//     permanentAddress.disabled = true;
//   } else {
//     permanentAddress.value = '';
//     permanentAddress.disabled = false;
//   }
// });
// write me a js function where I will click next and another page will appear
