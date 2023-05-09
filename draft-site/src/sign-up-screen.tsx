
import './sign-up-screen.css'

function SignUp() {
  return (
    <>
      <div className="sign-up">
        <div className="nav-top">
          <button id='sign-up-button'>Sign Up?</button>
          <button id='login-button'>Log in?</button>
        </div>
        <div className="google-signin">
          <button id='google-signin-button'>Sign in with G</button>
        </div>
        <div className="seperator">
          
          <hr className='solid'/>
          or
          <hr className='solid'/>
        </div>
        <div className="register">
          <form className='form'>
            <label>
              <span className='inputfield'>Username:</span>
              <input type="text" />
            </label>
            <label>
              <span className='inputfield'>Email:</span>
              <input type="text" />
            </label>
          </form>
          <form className='form'>
            <label>
              <span className='inputfield'>Password:</span>
              <input type="text" />
            </label>
            <label>
              {/* <span className='inputfield'>Birthday:</span> */}
              Birthday:
              <input type="text" />
            </label>
          </form>
        </div>
        <div className="signup-button">
          <button id='google-signin-button'>Sign Up</button>
        </div>
      </div>
    </>
  )
}

export default SignUp