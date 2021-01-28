import React, {useState} from 'react';
import {withCookies} from 'react-cookie';
import axios from 'axios';
import {Button} from '@material-ui/core';

/**
* @author
* @function Auth
**/

const Auth = (props) => {
    const [ username, setUsername ] = useState("");
    const [ password, setPassword ] = useState("");
    const [ loginFunction, setLoginFunction ] = useState(true);
    const [ errorMessage, setError ] = useState("");

    const auth = (event) =>{
        event.preventDefault();
        let form_data = new FormData();

        form_data.append('username', username);
        form_data.append('password', password);

        const postUri = loginFunction ? `&{process.env.REACT_APP_END_POINT}/api/token` : `${process.env.REACT_APP_END_POINT}/api/users`;

        axios.post(postUri, form_data, {
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then( res => {
            props.cookies.set('reg-token', res.data.token);
            window.location.href = "/";
        })
        .catch( error => {
            setError(error.response.data)
        });
    }

    const changeFunction = () =>{
        setLoginFunction(!loginFunction)
        setUsername("")
        setPassword("")
        setError("")
    }

    return(
        <div className="form central-placement">
        <form onSubmit={auth}>
          <div>
            <h3>{loginFunction ? 'ログイン' : 'サインイン'}</h3>
          </div>
          { errorMessage.non_field_errors ? <p className="red">{errorMessage.non_field_errors}</p> : null }
  
          <div className="form-element">
            <input type="text" name="username" value={username}
                className="form-element--username"
                onChange={(e) => setUsername(e.target.value)}
                placeholder="ユーザー名" />
            { errorMessage.username ? <p className="red">{errorMessage.username}</p> : null }
          </div>
          <div className="form-element">
            <input type="password" name="password" value={password}
                className="form-element--password"
                onChange={(e) => setPassword(e.target.value)}
                placeholder="パスワード" />
            { errorMessage.password ? <p className="red">{errorMessage.password}</p> : null }
            </div>
          <div className="form-element right-placement">
            <Button variant="contained" color="primary" type="submit" >{loginFunction ? 'ログイン' : 'サインイン'} </Button>
          </div>
          <div className="center-placement">
            <Button variant="contained" type="button" onClick={changeFunction}>{loginFunction ? 'アカウントを作成する' : 'ログインする'} </Button>
          </div>
        </form>
      </div>
    )

}

export default withCookies(Auth)