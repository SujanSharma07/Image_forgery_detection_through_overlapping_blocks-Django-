
function loadinganimation()
{

let x = document.getElementById("input_data").files.length;
if(x==0){
    alert("Please Select a Image")
} 
else
{
let ids = ["circles","one","two","three","pacman","top","bottom","left", "eye" ]

for(let i =0 ; i<ids.length;i++)
{

    document.getElementById(ids[i]).className = ids[i];
}
document.getElementById("processing_text").className = "loader";
document.getElementById("processing_text2").className = "loader2";

console.log("All Good")
}
}