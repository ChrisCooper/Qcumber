//
//  SearchViewController.h
//  Qcumber
//
//  Created by Chris Cooper on 11-12-30.
//  Copyright (c) 2011 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface SearchViewController : NSViewController


@property (weak) IBOutlet NSSearchField *searchField;
@property (weak) IBOutlet NSButton *advancedSearchButton;
@property (weak) IBOutlet NSTableView *resultsTableView;


@end
