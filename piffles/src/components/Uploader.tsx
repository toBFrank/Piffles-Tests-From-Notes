import React, {Component} from "react";
import { ChangeEvent } from "react";

/**
 * Component for uploading a file.
 * 
 * @author: Franco Bonilla
 * @version: 0.1.0
 * @since: 2023/04/27
 */
class Uploader extends Component {
    handleFileUpload(event: ChangeEvent<HTMLInputElement>) {
        const file = event.target.files?.[0];
        console.log(file);
    }

    render() {
        return (
            <div>
                <input 
                type="file" 
                onChange={this.handleFileUpload}
                accept="application/pdf" />
            </div>
        )
    }
}

export default Uploader;