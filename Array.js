function Array(number){
     for(let index = 0; index < number.length; index++) { 
     for(let indexa = 0; indexa < number.length-1; indexa++){
         for(let count = indexa + 1; count < number[index].length; count ++){
		     let change = number[index][count]
		    number[index][indexa] = number[index][count];
		    number[index][count] = change;
		}
	   }
      	}
   }
              return number;
 
let number = [
                [1, 2, 3]
                [4, 5, 6]
                [7, 8, 9]
            ];  
            
            
            
            
        let result = Array(number)
        console.log(result); 
            
  
  
		      
 

 
