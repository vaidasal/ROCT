import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { SharingService } from './services/sharing.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  title = 'ROCTool';

  loader!: boolean;
  subscription!: Subscription;

  constructor(private share: SharingService) {}

  ngOnInit() {
    this.subscription = this.share.loaderSource.subscribe(loader => this.loader = loader);
    this.newLoader(false);
  }

  newLoader(load: boolean) {
    this.share.changeLoader(load);
  }

}
