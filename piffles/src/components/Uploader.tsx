import { type } from "os";
import React, {Component} from "react";
import { ChangeEvent } from "react";
import styled from "styled-components";



const InputText = styled.input.attrs({type: "text"})`
    width: 100%;
    height: 200px;
    max-width: 500px;
    max-height: 500px;
    padding: 10px;
    margin: 10px;
    resize: vertical;
    overflow: auto;
    `;

    
type State = {
    file: File | undefined;
    text: string;
};



/**
 * Component for uploading a file.
 * 
 * @author: Franco Bonilla
 * @version: 0.1.0
 * @since: 2023/04/27
 */
class Uploader extends Component<{}, State> {
    constructor(props: {}) {
        super(props);
        this.handleTextWrite = this.handleTextWrite.bind(this);
        this.handleFileUpload = this.handleFileUpload.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

        this.state = {
            file: undefined,
            text: "",
        };
    }

    handleTextWrite(event: ChangeEvent<HTMLInputElement>) {
        const {value} = event.target;
        this.setState({text: value});
    }
    handleFileUpload(event: ChangeEvent<HTMLInputElement>) {
        const file = event.target.files?.[0];
        this.setState({file: file});
    }
    handleSubmit(event: React.FormEvent<HTMLFormElement>) {
        // alert whether the file was uploaded or the text was pasted
        event.preventDefault();
        if (this.state.file) {
          alert("File uploaded!");
        } else if (this.state.text) {
          alert("Text written!");
        } else {
          alert("Please upload a file or enter some text.");
        }
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit} >
                <div>
                    <input 
                    type="file" 
                    onChange={this.handleFileUpload}
                    accept="application/pdf" />
                </div>
                <h3>OR</h3>
                <div>
                    <InputText
                    type="text"
                    onChange={this.handleTextWrite} />
                </div>
                <div>
                <button type="submit">Submit</button>
                </div>
            </form>
        )
    }
}

export default Uploader;