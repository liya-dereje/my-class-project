import { header } from './header' ;
import {Menu} from './menu';
const price = 90
function App() {
return(
<>
    <h1>The price is {price} </h1>
    <header price = {price}/>
    <menu/>
</>
);}

export default App