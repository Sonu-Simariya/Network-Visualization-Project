function graph_1 (){
  var ctx = document.getElementById('ipStatusChart').getContext('2d');
  var ipStatusChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels: {{ labes|safe }},
          datasets: [{
              data: {{ dat|safe }},
              backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(54, 162, 235)',
                  'rgb(255, 206, 86)',
                  'rgb(15, 12, 92)',
                  'rgb(153, 102, 255)'
              ]
          }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Status',
            color:'red'
            
          }
        }
      },
  });
}
function graph_2(){
  var ctx = document.getElementById('StatusChart').getContext('2d');
  var StatusChart = new Chart(ctx, {
      type: 'pie',
      data: {
          labels:{{ labels|safe }},

          datasets: [{
              data: {{ dat|safe }},
              backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(54, 162, 235)',
                  'rgb(255, 206, 86)',
                  'rgb(15, 12, 92)',
                  'rgb(153, 102, 255)'
              ]

          }],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Ip',
            color:'red'
            
          }
        }
      },
      
  });
  
}


function toggleFullscreen() {
      var doc = window.document;
      var docEl = doc.documentElement;

      var requestFullScreen = docEl.requestFullscreen || docEl.mozRequestFullScreen || docEl.webkitRequestFullScreen || docEl.msRequestFullscreen;
      var cancelFullScreen = doc.exitFullscreen || doc.mozCancelFullScreen || doc.webkitExitFullscreen || doc.msExitFullscreen;

      if (!doc.fullscreenElement && !doc.mozFullScreenElement && !doc.webkitFullscreenElement && !doc.msFullscreenElement) {
          requestFullScreen.call(docEl);
          document.body.style.backgroundColor = '#fff';
          document.getElementById("btt").innerHTML="Exit Screen"
          
           // Set background color to white
      } else {
          cancelFullScreen.call(doc);
          document.body.style.backgroundColor = '';
          

        
          document.getElementById("btt").innerHTML="Full Screen"  // Reset background color to default
      }
  }