function InitializeVanta(){
    let vantaEffect1, vantaEffect2;


    vantaEffect1 = VANTA.NET({
        el: "#hero",
        mouseControls: true,
        touchControls: true,
        minHeight: 200.00,
        minWidth: 200.00,
        scale: 1.00,
        scaleMobile: 1.00,
        color: 0x007bff,       
        backgroundColor: 0x000000,  
        points: 20.00,           
        maxDistance: 20.00,      
        spacing: 15.00 
      });
  
      vantaEffect2 = VANTA.NET({
        el: "#hero2",
        mouseControls: true,
        touchControls: true,
        minHeight: 200.00,
        minWidth: 200.00,
        scale: 1.00,
        scaleMobile: 1.00,
        color: 0x007bff,       
        backgroundColor: 0x000000,  
        points: 20.00,           
        maxDistance: 20.00,      
        spacing: 15.00 
      });
}
function HandleServiceForm(){
    const steps = document.querySelectorAll(".form-step");
    const nextBtns = document.querySelectorAll(".next-btn");
    const prevBtns = document.querySelectorAll(".prev-btn");
    let progressBar = document.querySelector("#inner-progress");
    let currentStep = 0;

    function validateCurrentStep(stepIndex) {
        const inputs = steps[stepIndex].querySelectorAll("input, select, textarea");
        for (let input of inputs) {
            if (input.hasAttribute("required") && input.value.trim() === "") {
                return false;
            }
        }
        return true;
    }

    nextBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            if (!validateCurrentStep(currentStep)) {
                DisplayNotification("Please fill in all required fields.");
                return;
            }
            if (currentStep < steps.length - 1) {
                steps[currentStep].classList.remove("active");
                currentStep++;
                progressBar.style.width = `${(currentStep) / (steps.length - 1) * 100}%`;
                steps[currentStep].classList.add("active");
            }
        });
    });

    prevBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            if (currentStep > 0) {
                steps[currentStep].classList.remove("active");
                currentStep--;
                progressBar.style.width = `${(currentStep) / (steps.length - 1) * 100}%`;
                steps[currentStep].classList.add("active");
            }
        });
    });
}

function SubmitServiceForm() {
    const $form = $("#service-form");
    $form.on("submit", function(e) {
        e.preventDefault();

        const formData = new FormData(this);

        $.ajax({
            url: $form.attr("action"),
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function() {
                DisplayNotification("Form submitted successfully!");
                $form[0].reset();
            },
            error: function(xhr) {
                if (xhr.status===400){
                    DisplayNotification(xhr.responseJSON.error)
                }
                else{
                    DisplayNotification('Something went wrong')
                }
            }
        });
    });
}

$(document).ready(function() {
    InitializeVanta();
    AOS.init();
    HandleServiceForm();
    SubmitServiceForm();
});
