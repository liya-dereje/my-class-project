export function Dish({name, id , price}){
    return(
        <div className="dish">
            <h1>Addis Eats</h1>
            <h3>{id}</h3>
            <h3>{name}</h3>
            <p>{price}ETB</p>
        </div> );
}