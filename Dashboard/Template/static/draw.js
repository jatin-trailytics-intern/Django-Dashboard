const tclick = document.querySelector("#click_group");
const tad_sales = document.querySelector('#sale_group');
const tview = document.querySelector('#impression_group');
const torders = document.querySelector('#order_group');
const tad_spend = document.querySelector('#spend_group');
const links = document.querySelectorAll(".nav-link");
const ctr = document.querySelector("#ctr_group");
const cvr = document.querySelector("#cvr_group");
const acos = document.querySelector("#acos_group");






function color_box(list){
var colors = []
var col = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
for(var i=0; i <= list.length; i++){
  color = "#" + col[Math.round((Math.random() *10))] 
          + col[Math.round((Math.random() *10))] 
          + col[Math.round((Math.random() *10))] 
          + col[Math.round((Math.random() *10))] 
          + col[Math.round((Math.random() *10))]
          + col[Math.round((Math.random() *10))];
  colors.push(color);  
}
return colors;
}

links.forEach(function(link){
  link.addEventListener('click', function(){
    link.classList.add("fw-bolder")
  })
})



console.log(datamapping);

// Charts.js


const range = []

const labels = datamapping['date'];


const data = {
  labels: labels,
  datasets: [
    {
      label: 'Views',
      data: datamapping['impressions'],
      backgroundColor:'rgba(0, 255, 0, .6)',
      borderColor: 'rgba(0, 255, 0, 1)' ,
    },
  ]
};




const config = {
  type: 'line',
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Clicks'
      }
    }
  },
};



const chart =  new Chart("bar", config)




function handler(chart, val=0) {
  const data = chart.data;
  const newDataset = [{
      label:"click",
      backgroundColor:'rgba(255, 0, 0, .6)',
      borderColor: 'rgba(255, 0, 0, 1)' ,
      data: datamapping['clicks'] 
},
{
      label:"impressions",
      backgroundColor:'rgba(0, 255, 0, .6)',
      borderColor: 'rgba(0, 255, 0, 1)' ,
      data: datamapping['impressions'] 
},
{
      label:"adsales",
      backgroundColor:'rgba(0, 0, 255, .6)',
      borderColor: 'rgba(0, 0, 255, 1)' ,
      data: datamapping['cdcr'] 
},

{
      label:"orders",
      backgroundColor:'rgba(100, 100, 100, .6)',
      borderColor: 'rgba(100, 100, 100, 1)' ,
      data: datamapping['cdcu'] 
},
{
      label:"adspends",
      backgroundColor:'#2314ff',
      borderColor: '#2314ff' ,
      data: datamapping['ads_spend'] 
},
{
      label:"ctr",
      backgroundColor:'#ccfe22',
      borderColor: '#ccfe22' ,
      data: datamapping['ctr'] 
},
{
      label:"cvr",
      backgroundColor:'#cc88aa',
      borderColor: '#cc88aa' ,
      data: datamapping['cvr'] 
},
{
      label:"Acos",
      backgroundColor:'#ff2277',
      borderColor: '#ff2277' ,
      data: datamapping['roi'] 
},

]
if(chart.data.datasets.length==2){
  chart.data.datasets.shift();
}
  chart.data.datasets.push(newDataset[val]);
  chart.update();
}  














tclick.addEventListener('click', ()=>{
  handler(chart, 0);  
})

tad_spend.addEventListener('click', ()=>{
  handler(chart, 4)
})

tad_sales.addEventListener('click', ()=>{
  handler(chart, 2)
})

tview.addEventListener('click', ()=>{
  handler(chart, 1)
})

torders.addEventListener('click', ()=>{
  handler(chart, 3)
  })


ctr.addEventListener('click', ()=>{
  handler(chart, 5)
  })


cvr.addEventListener('click', ()=>{
  handler(chart, 6)
  })


acos.addEventListener('click', ()=>{
  handler(chart, 7)
  })







