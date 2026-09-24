const input = document.getElementById("templateInput");
const templateImage = document.getElementById("templateImage");
const testImageInput = document.getElementById("testInput");        
const testImagePreview = document.getElementById("testImagePreview"); 
testImageInput.addEventListener("change", function(){
    const file2 = testImageInput.files[0];
    console.log(file2);
    testImagePreview.src = URL.createObjectURL(file2);
});
input.addEventListener("change", function(){
    const file1 = input.files[0]
    console.log(file1)
    templateImage.src = URL.createObjectURL(file1)
})
const detectButton = document.getElementById("processButton");
const outputImageEdges = document.getElementById("outputImageEdges");
detectButton.addEventListener("click", async function(){
    const file2 = testImageInput.files[0]
    const formData = new FormData();
    formData.append("image", file2);
    const response = await fetch("http://127.0.0.1:5000/detect", {
        method: "POST",
        body: formData
    });
    const result = await response.blob();
    outputImageEdges.src = URL.createObjectURL(result);
    console.log(result);
})
const subtractButton = document.getElementById("subtractButton");
const outputImageSubtract = document.getElementById("outputImageSubtract");
subtractButton.addEventListener("click", async function(){
    const file1 = input.files[0]
    const file2 = testImageInput.files[0]
    const formData = new FormData();
    formData.append("image1", file1);
    formData.append("image2", file2);
    const response = await fetch("http://127.0.0.1:5000/subtract", {
        method: "POST",
        body: formData
    });
    const result = await response.blob();
    outputImageSubtract.src = URL.createObjectURL(result);
    console.log(result);
})