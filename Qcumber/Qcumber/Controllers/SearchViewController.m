//
//  SearchViewController.m
//  Qcumber
//
//  Created by Chris Cooper on 11-12-30.
//  Copyright (c) 2011 __MyCompanyName__. All rights reserved.
//

#import "SearchViewController.h"

@implementation SearchViewController

@synthesize searchField;
@synthesize advancedSearchButton;
@synthesize resultsTableView;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Initialization code here.
    }
    
    return self;
}

@end
