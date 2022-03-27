import axios from "../helpers/axios";
import { authConstants } from "./constants"

export const getData = () => {
    return async (dispatch) => {
        console.log("hii getaData here");
        const data = {
            "title": "Yash Nistane",
            "type": "Admi",
            "price": 50,
            
        }
        try {
           
            const res = await axios.get("/list/");
            console.log(res);
            // if(res.status == 200){
            //     dispatch({ type: authConstants.GET_DATA,
            //     payload:res.data,
            //     });
            // }
        } catch (error) {
            console.log(error);
        }
    }
}
