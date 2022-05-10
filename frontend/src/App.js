import React, {Component} from "react"
import axios from 'axios'


class App extends Component{
  state = {
    todos:[]
  };

  componentDidMount(){
    this.getTodos();
  }
  getTodos(){
    axios
    .get('http://127.0.0.1:8000/api/booklist/')
    .then(res => {
      this.setState({todos:res.data});
    })
    .catch(err=>{
      console.log(err)
    })
  }
  render(){
    return(
      <div>
        {
          this.state.todos.map(item=>(
            <div key={item.id}>
              <h1>{item.title}</h1>
              <span>{item.description}</span>
            </div>
          ))}
      </div>
    );
  }
}

export default App;
// const list =[
//   {
//     "id": 3,
//     "title": "A Tale of Two Cities",
//     "description": "880-02 Di 1 ban.",
//     "slug": "technology",
//     "image": "http://127.0.0.1:8000/media/books/9.jpg",
//     "price": 150,
//     "pub_date": "2022-05-07",
//     "category": 4,
//     "author": 1
//   },
//   {
//     "id": 2,
//     "title": "Eight cousins, or, The aunt hill",
//     "description": "Complete authorized edition published by arrangement with little brown and company",
//     "slug": "detective",
//     "image": "http://127.0.0.1:8000/media/books/5.jpg",
//     "price": 50,
//     "pub_date": "2022-05-07",
//     "category": 3,
//     "author": 1
//   }
// ]

// class App extends Component{
//   constructor(props){
//     super(props);
//     this.state = { list };
//   }
//   render(){
//     return (
//       <div>
//         {this.state.list.map(item=>(
//           <div key = {item.id}>
//             <h1>{item.title}</h1>
//             <p>{item.description}</p>
//           </div>
//         ))}
//       </div>
//     );
//   }
// }
// export default App;
