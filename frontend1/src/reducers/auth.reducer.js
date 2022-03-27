import { authConstants } from "../actions/constants";

const initState = {
  dataa:[],
  token: null,
  user: {
    firstname: "",
    lastname: "",
    email: "",
    picture: "",
  },
  authenticate: false,
  authenticating: false,
  loading: false,
  errorMessage: null,
  
 
};

export default (state = initState, action) => {
  //console.log(action);
  switch (action.type) {

    case authConstants.GET_DATA:
        state = {
          ...state,
          dataa: action.payload,
        };
        break;
  }
  return state;
};
