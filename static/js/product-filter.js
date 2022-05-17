// $(document).ready(function(){
//     $(".filter-checkbox").on('click', function(){
//         var filterObj = {};
//         $(".filter-checkbox").each(function(index, ele){
//             var filterValue = $this.val();
//             var filterKey = $this.data('filter');
//             console.log(filterValue, filterKey);
//         });
//     });
// });

console.log('hello Ajax')

let filter = document.getElementsByClassName('filter-checkbox');

var _filterObj = []

for(var i=0; i<filter.length; i++){
    filter[i].addEventListener('click', function(){


        var filter = this.dataset.filter
        var value = this.dataset.value
        _filterObj[value] = filter


        
        console.log('filter:', filter)
        console.log('Value:', value)

        console.log(_filterObj)

        filterProduct()
    })
} 



function filterProduct() {
    console.log("btn click")

    //Instantiate an xhr obj
    const xhr= new XMLHttpRequest();

    //open object
    xhr.open('GET', '/accessories', true);

    //on progress
    xhr.onprogress = function(){
        console.log('on progress');
    }

    //when response is ready
    xhr.onload = function(){
        // console.log(this.responseText);
    }

    //send request
    xhr.send();
}