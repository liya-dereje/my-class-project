import {Dish} from "./Dish"

const menu = [
{ id: 1, name: "Doro Wat", price: 240 },
{ id: 2, name: "Shiro", price: 120 },
{ id: 3, name: "Tibs", price: 280 },
];

export function menu() {
return (
<div>
{menu.map(d =>
<Dish id={d.id} name={d.name}

price={d.price} />
)}
</div>
);
}